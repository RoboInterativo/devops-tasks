FROM hlebsur/pet_clinic_not_full:latest as build
RUN ./mvnw compile

EXPOSE 8080
FROM eclipse-temurin:17-jre-jammy as production
COPY --from=build /app/target/spring-petclinic-*.jar /spring-petclinic.jar
CMD ["java", "-Djava.security.egd=file:/dev/./urandom" "-jar", "/spring-petclinic.jar"]
HEALTHCHECK --start-period=1m CMD curl -f http://localhost:8080/ || exit 1
