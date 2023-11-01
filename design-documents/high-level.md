# High-level design
## Application Architecture
### Diagram
[Link to Lucidchart]([https://lucid.app/lucidchart/46d3f75f-e18d-434b-a764-33db2f0f6cc6/edit?view_items=uOSIrlZhB-Ub%2COETI-mDHDvcp%2CVFTIlm.skYEQ%2CiPSIY5i94E.N%2CEFTIn17EvMsk%2CE0SIV1gqAg.4%2C6WSIEUyOVW-~%2CuUSIzU8aqxHS%2CaGTIgjE.wFU-%2CnGTILsVdm3X1%2CrUSIGnVn_PLG%2CgFTICVsIFrp5%2CEGTIGg0ykW3C&invitationId=inv_1814f6ab-0de8-45a3-8abf-234cca2ee2c0](https://lucid.app/lucidspark/invitations/accept/inv_7fe0188e-fcb1-4dcc-981c-2f0019bb9fdc))
### Step to deploy to the Cloud
  1. We choose render.com to host the web servers.
  2. Packaging our application in to docker containers.
  3. Setup dababase on MongoDB.
  4. Prepare for scalability. Use load balancers or other close services to handle large traffic.
### Deployment Pipeline
  1. Code is stored in the cloud repository(Github).
  2. The code is compiled or built, generating artifacts (e.g., binaries, libraries).
  3. Unit tests are run to ensure that individual code components work as expected.
  4. Build docker container images and run successfully in local environment
  5. Once all tests and checks pass, the changes are deployed to the production environment. 
### Frontend Wireframes
[Link to Figma](https://www.figma.com/file/x1LuRa2y4Wm83u2NRH9tiy/Untitled?type=design&node-id=0%3A1&mode=design&t=pX7MuVYy0nwR7qRI-1)
### Description of Backend Modules
