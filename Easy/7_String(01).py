def search_substr():
    subst=input("подстрока: ")
    st=input("строка: ")
    if subst.lower() in st.lower():
        print ("Есть контакт!")
    else:
        print ("Мимо!")
search_substr()
