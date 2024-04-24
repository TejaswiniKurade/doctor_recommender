# import streamlit as st
# if 'specialist_df' not in st.session_state:
#     st.session_state['specialist_df'] = None

# if 'doctor_df' not in st.session_state:
#     st.session_state['doctor_df'] = None

# if 'predicted_disease' not in st.session_state:
#     st.session_state['predicted_disease'] = None
    
# specialist_df=st.session_state['specialist_df']
# doctor_df=st.session_state['doctor_df'] 
# predicted_disease=st.session_state['predicted_disease']



# specialist_df_filtered = specialist_df[specialist_df['Disease'] == predicted_disease]
# specialists = specialist_df_filtered['Specialist'].tolist()
#     # Assuming 'Specialist' column exists in doctor.df
# specialist_doctors = doctor_df[doctor_df['Specialization'].isin(specialists)]
# preference = st.selectbox("Select your preference:", options=["Distance", "Experience"])
# def doctor_score(doctor_row, preference):
#  experience = doctor_row['ExperienceYears']
#  rating = doctor_row['Rating']
#  distance = doctor_row['Distance']  # Assuming distance from user's location

# # Default weights
#  w_exp = 0.3
#  w_rating = 0.3
#  w_distance = 0.3

# # Adjust weights based on user's preference
#  if preference == "Experience":
#      w_exp = 0.4
#  elif preference == "Distance":
#      w_distance = 0.4
#  elif preference == "Distance":
#      w_rating = 0.4

#  return w_exp * experience + w_rating * rating - w_distance * distance 
         
# if 'doctor_score' in globals(): 
#         top_doctor = specialist_doctors.apply(lambda row: doctor_score(row, preference), axis=1).idxmax()
#         top_doctor_info = specialist_doctors.loc[top_doctor]
#         st.subheader("Top Recommended Doctor:")
#         st.write(f"Name: {top_doctor_info['Doctor Name']}")
#         st.write(f"Speciality: {top_doctor_info['Specialization']}")
#         st.write(f"Experience: {top_doctor_info['ExperienceYears']} years")
#         st.write(f"Average Rating: {top_doctor_info['Rating']}")           
