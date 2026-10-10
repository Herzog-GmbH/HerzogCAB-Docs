# Glossary

!!! abstract "Reference — Technical terms around Herzog CAB and braiding"

The column **Term** shows the English term used in the program; the German term from
the German interface and German machine documentation follows in brackets.

| Term | Meaning |
|---|---|
| **Module** (Baustein) | Licensed scope of functions in the customer account, e.g. *Herzog CAB Full Version*, *Herzog CAB Designer* or *Herzog CAB Trial*. Each module has seats and a term, see [Customer account and invitation](../setup/account.md). |
| **Setup** (Besetzung) | Pattern by which the carriers occupy the positions of a braiding machine. Herzog CAB distinguishes **Standard setup** (1-1, all positions occupied), **Tandem setup** (2-2, see **Tandem**) and **Half setup** (1-3, only every second position occupied). |
| **Cloud sync** (Cloud-Abgleich, Cloud-Upload) | Automatic synchronisation of the desktop app's workspace folder with the workspace of the web app: up to the web app and — can be switched off — changes from the web app back; in case of conflicts the desktop wins. See [Licence and cloud](../admin/settings/license.md). |
| **CmActLicense** (CmActLicense) | Software licence from Wibu CodeMeter, bound to the fingerprint of the computer (existing customers). |
| **CmDongle** (CmDongle) | USB licence dongle from Wibu CodeMeter. |
| **Edition** (Edition) | What an installation currently is: *Full version*, *Designer version* or *Trial version* – derived from the modules of the account or the Feature Code of the dongle. |
| **Entra ID** (Entra ID) | Microsoft Entra ID (formerly Azure Active Directory) – Microsoft's cloud directory service. Herzog CAB can let users sign in through it, see [Authentication](../admin/authentication.md). |
| **Ply count** (Fachung) | Number of threads per carrier. |
| **Fineness / Titer** (Feinheit / Titer) | Program term for **linear density** – mass per unit length (tex, dtex, den …). |
| **Braiding angle** (Flechtwinkel) | Angle at which a strand runs in the braid — at Herzog measured to the transverse direction by default, in the technical literature usually to the braid axis; the two add up to 90°. The reference can be selected under *Settings > General > Braiding angle*. |
| **Track** (Gangbahn) | The path along which the carriers run through the braiding machine. In the Designer, the movement of the carriers on the track can be shown as an animation, see [Setup and track animation](../designer/animation.md). |
| **Braid density** (Geflechtsdichte) | Program term for the density of the braid; the associated measure is the **lay length** (German *Schlaglänge*, also called *Verlegelänge*). |
| **Herzog CAB Web / web app** (Herzog CAB Web / Web-App) | Herzog CAB in the browser at app.herzog-cab.com, see [Web app](../web/index.md). |
| **Hollow braid** (Hohlgeflecht) | Tube- or hose-shaped braid (also called *tubular braid*). In the program this calculation group is called **Hollow braid** (not “tubular braid”). |
| **Horngear** (Flügelrad) | Wheel of the braiding machine with slots that guides the carriers along their path and hands them over to the neighbouring horngear. |
| **Carrier** (Klöppel) | Bobbin holder on a braiding machine. |
| **Customer account** (Kundenkonto) | A company's account on the Herzog licence server: modules, seats, computers and users. Managed in the **licence portal**. |
| **LDAP** (LDAP) | *Lightweight Directory Access Protocol* – standard protocol for directory services such as Active Directory. Herzog CAB can sign in and import users through it, see [Authentication](../admin/authentication.md). |
| **Licence portal** (Lizenzportal) | Web interface for the customer account at license.herzog-cab.com, see [Licence portal](../portal/index.md). |
| **Maintenance Tool** (Maintenance-Tool) | Update/uninstall tool of Herzog CAB. |
| **Lease** (Miete) | The licence server's confirmation with which a computer holds its seat and may also work without a connection. From version 2.1.0, the program holds its seat as long as it is running and continues to work without a connection for up to 24 hours. An **offline lease** holds the seat for up to 30 days, even when the program is closed. Up to version 2.0.0, the normal lease was called **regular lease** and held the seat for seven days. |
| **Packing braid** (Packungsgeflecht) | Braid type of the packing braider with horngears in a grid (2-, 3-, 4-track or round; 8 to 52 carriers depending on the version), braided over several tracks. |
| **PCD** (PCD) | Pitch Circle Diameter (German *Flügelteilkreis-Durchmesser*). |
| **Seat** (Platz) | Unit of the licence: one person who is currently working. Each computer on which Herzog CAB is running takes one seat, as does each person in the browser. Program and browser at the same time take two seats. |
| **Profile** (Profil) | Client/workspace – connects a user with a workspace and the web server options. |
| **Square braid** (Quadratgeflecht) | Braid with a square cross-section, braided from 8 to 36 carriers on 2 tracks. |
| **Regular lease** (Regelmiete) | See **Lease**. |
| **Role** (Rolle) | Bundle of permissions (Administrator, Editor, Viewer …). |
| **Lay length** (Schlaglänge) | Axial advance for one full revolution of a strand around the product. |
| **Cores** (Seelen) | Core inserts in the soutache braid: two threads through the axes of the horngears that are braided over. |
| **Soutache braid** (Soutachegeflecht) | Cord braid on two horngears with an odd number of carriers (3–11), optionally with two cores. |
| **Spiral braid** (Spiralgeflecht) | Braid type of the spiral braider with 4 horngears in a fixed outer ring (12 or 20 carriers). |
| **Winding order** (Spulauftrag) | Separate order type for the winding department – analogous to the braiding order, but for filling bobbins on a bobbin winding machine, optionally linked to a braiding order. |
| **Bobbin** (Spule) | Holder of the yarn/wire on the carrier. |
| **Winding head** (Spulstelle) | Single winding position on a bobbin winding machine. |
| **Tandem** (Tandem) | Setup variant in which two adjacent machine positions together form one strand (2-2). Important, for example, for strand braids to avoid collisions. |
| **Winding technology** (Wickeltechnik) | Method by which a bobbin winding machine lays the material onto the bobbin – a master data item of a bobbin winding machine. |
| **Workspace / workspace folder** (Workspace / Arbeitsverzeichnis) | Data folder with master data, orders, designs and print templates. |
| **Second factor (2FA)** (Zweiter Faktor) | Additional code from an authenticator app when signing in to the customer account – for the portal, desktop app and web app, see [Password, second factor and name](../portal/security.md). |
