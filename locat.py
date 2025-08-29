import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# ------------------ Streamlit Config ------------------
st.set_page_config(page_title="📱 Phone Tracker Demo", page_icon="📳", layout="centered")
st.title("📳 Phone Number & Location Tracker (Educational Demo)")

# ------------------ Phone Number Tracking ------------------
phone_input = st.text_input("Enter a phone number with country code (e.g., +2348012345678):")

if phone_input:
    try:
        # Parse number
        parsed_number = phonenumbers.parse(phone_input)

        # Get details
        country = geocoder.description_for_number(parsed_number, "en")
        sim_carrier = carrier.name_for_number(parsed_number, "en")
        tz = timezone.time_zones_for_number(parsed_number)

        # Show info (cleaner output with 📳 and 🗺️)
        st.subheader("📳 Number Info")
        st.write(f"🗺️ **Country:** {country}")
        st.write(f"📡 **Carrier:** {sim_carrier if sim_carrier else 'Unknown'}")
        st.write(f"⏰ **Timezone:** {', '.join(tz) if tz else 'Unknown'}")

        # Map lookup
        geolocator = Nominatim(user_agent="phone_locator", timeout=10)
        location = geolocator.geocode(country)

        if location:
            m = folium.Map(location=[location.latitude, location.longitude], zoom_start=5)
            folium.Marker(
                [location.latitude, location.longitude],
                popup=f"📳 {country}\nCarrier: {sim_carrier}",
                icon=folium.Icon(color="blue", icon="phone", prefix="fa")
            ).add_to(m)

            st.subheader("🗺️ Approximate Country Location")
            st_folium(m, width=700, height=500)
        else:
            st.warning("⚠️ Could not find location on map.")

    except Exception as e:
        st.error(f"Error: {e}")

# ------------------ Free Search by Country/State/City ------------------
st.subheader("🌍 Search Any Location in the World")
location_search = st.text_input("Enter a country, state, or city:")

if location_search:
    try:
        geolocator = Nominatim(user_agent="world_locator", timeout=10)
        loc = geolocator.geocode(location_search)

        if loc:
            m2 = folium.Map(location=[loc.latitude, loc.longitude], zoom_start=6)
            folium.Marker(
                [loc.latitude, loc.longitude],
                popup=f"🗺️ {location_search}",
                icon=folium.Icon(color="green", icon="map-marker", prefix="fa")
            ).add_to(m2)

            st.success(f"✅ Found {location_search} at 📍 Lat: {loc.latitude}, Lon: {loc.longitude}")
            st.subheader("🗺️ Real Location on Map")
            st_folium(m2, width=700, height=500)
        else:
            st.warning("⚠️ Could not find that location.")
    except Exception as e:
        st.error(f"Error: {e}")
