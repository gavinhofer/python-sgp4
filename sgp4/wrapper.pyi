from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from . import vallado_cpp

class Satrec(vallado_cpp.Satrec):
    """High-speed computation of satellite positions and velocities.

    Attributes
    ----------
    a (float): Semi-major axis (km).
    alta (float): Apogee altitude (km).
    altp (float): Perigee altitude (km).
    am (float): Mean motion (radians/minute).
    argpdot (float): Argument of perigee rate (radians/minute).
    argpo (float): Argument of perigee (rad).
    bstar (float): B* drag term (1/earth radii).
    classification (str): Classification (U=Unclassified).
    ecco (float): Eccentricity.
    elnum (int): Element number.
    em (float): Eccentric anomaly (radians).
    ephtype (int): Ephemeris type.
    epochdays (float): Days since epoch.
    epochyr (int): Year of epoch.
    error (int): Error code.
    gsto (float): Greenwich sidereal time (radians).
    im (float): Inclination (radians).
    inclo (float): Inclination (radians).
    intldesg (str): International designator.
    j2 (float): J2 harmonic.
    j3 (float): J3 harmonic.
    j3oj2 (float): J3 divided by J2.
    j4 (float): J4 harmonic.
    jdsatepoch (float): Julian date of epoch.
    jdsatepochF (float): Fractional part of jdsatepoch.
    mdot (float): Mean motion derivative (radians/minute^2).
    method (str): Method (n=SGP4, d=SDP4).
    mm (float): Mean anomaly (radians).
    mo (float): Mean anomaly, wrapped to 0 to 2pi (radians).
    mu (float): Gravitational constant (km^3/s^2).
    nddot (float): Second derivative of mean motion (radians/minute^3).
    ndot (float): First derivative of mean motion (radians/minute^2).
    nm (float): Mean motion (radians/minute).
    no (float): Mean motion (radians/minute).
    no_kozai (float): Mean motion (radians/minute).
    nodedot (float): Right ascension of ascending node rate (radians/minute).
    nodeo (float): Right ascension of ascending node (radians).
    om (float): Argument of perigee (radians).
    operationmode (str): Operation mode (a=analytical, m=modified).
    radiusearthkm (float): Radius of the Earth (km).
    revnum (int): Revolution number at epoch.
    satnum (int): Satellite number.
    t (float): Time since epoch (minutes).
    tumin (float): Minutes in one time unit.
    xke (float): Reciprocal of tumin.
    """

    a: float
    alta: float
    altp: float
    am: float
    argpdot: float
    argpo: float
    bstar: float
    classification: str
    ecco: float
    elnum: int
    em: float
    ephtype: int
    epochdays: float
    epochyr: int
    error: int
    gsto: float
    im: float
    inclo: float
    intldesg: str
    j2: float
    j3: float
    j3oj2: float
    j4: float
    jdsatepoch: float
    jdsatepochF: float
    mdot: float
    method: str
    mm: float
    mo: float
    mu: float
    nddot: float
    ndot: float
    nm: float
    no: float
    no_kozai: float
    nodedot: float
    nodeo: float
    om: float
    operationmode: str
    radiusearthkm: float
    revnum: int
    satnum: int
    t: float
    tumin: float
    xke: float

    def sgp4(
        self, jd: float, fr: float
    ) -> tuple[int, tuple[float, float, float], tuple[float, float, float]]:
        """

        Parameters
        ----------
        jd (float): Julian date.
        fr (float): Fractional part of the Julian date.

        Returns
        -------
        error (int): Error code.
        r (tuple[float, float, float]): Satellite position vector in km.
        v (tuple[float, float, float]): Satellite velocity vector in km/s.
        """
        ...
    def sgp4_array(
        self,
        jd: NDArray[np.floating],
        fr: NDArray[np.floating],
    ) -> tuple[NDArray[np.uint8], NDArray[np.float64], NDArray[np.float64]]:
        """Compute positions and velocities for the times in a NumPy array.

        Given NumPy arrays ``jd`` and ``fr`` of the same length that
        supply the whole part and the fractional part of one or more
        Julian dates, return a tuple ``(e, r, v)`` of three vectors:

        * ``e``: nonzero for any dates that produced errors, 0 otherwise.
        * ``r``: position vectors in kilometers.
        * ``v``: velocity vectors in kilometers per second.

        Parameters
        ----------
        jd (NDArray[np.floating]): Julian date.
        fr (NDArray[np.floating]): Fractional part of the Julian date.

        Returns
        -------
        error (NDArray[np.uint8]): Error code.
        r (NDArray[np.float64]): Satellite position vector in km.
        v (NDArray[np.floating]): Satellite velocity vector in km/s.
        """
        ...
    def sgp4_tsince(
        self, tsince: float
    ) -> tuple[int, tuple[float, float, float], tuple[float, float, float]]:
        """Compute position and velocity for a given time since epoch.

        Parameters
        ----------
        tsince (float): Time since epoch (minutes).

        Returns
        -------
        error (int): Error code.
        r (tuple[float, float, float]): Satellite position vector in km.
        v (tuple[float, float, float]): Satellite velocity vector in km/s.
        """
        ...
    def sgp4init(
        self,
        whichconst: int,
        opsmode: str,
        satnum: int,
        epoch: float,
        bstar: float,
        ndot: float,
        nddot: float,
        ecco: float,
        argpo: float,
        inclo: float,
        mo: float,
        no_kozai: float,
        nodeo: float,
    ) -> None:
        """Initialize a satellite record from orbital elements.

        Parameters
        ----------
        whichconst (int): Which set of constants to use.  1 for WGS72, 2 for WGS84.
        opsmode (str): 'a' for "afspc" mode, 'i' for improved mode.
        satnum (int): Satellite number.
        epoch (float): Epoch in days since 1949 December 31 00:00 UT.
        bstar (float): Ballistic drag coefficient B* (1/earth radii).
        ndot (float): First time derivative of the mean motion (radians/minute^2).
        nddot (float): Second time derivative of the mean motion (radians/minute^3).
        ecco (float): Eccentricity.
        argpo (float): Argument of perigee (radians).
        inclo (float): Inclination (radians).
        mo (float): Mean anomaly (radians).
        no_kozai (float): Mean motion (radians/minute).
        nodeo (float): Right ascension of ascending node (radians).
        """
        ...
    @classmethod
    def twoline2rv(cls, line1: str, line2: str) -> Satrec:
        """Create a Satrec object from a two-line element (TLE) set.

        Parameters
        ----------
        line1 (str): First line of the TLE.
        line2 (str): Second line of the TLE.

        Returns
        -------
        satrec (Satrec): Satellite record.
        """
        ...

class SatrecArray(vallado_cpp.SatrecArray):
    """Satellite record array."""

    def sgp4(
        self, jd: NDArray[np.floating], fr: NDArray[np.floating]
    ) -> tuple[NDArray[np.uint8], NDArray[np.float64], NDArray[np.float64]]:
        """Compute positions and velocities for the times in a NumPy array.

        Given NumPy arrays ``jd`` and ``fr`` of the same length that
        supply the whole part and the fractional part of one or more
        Julian dates, return a tuple ``(e, r, v)`` of three vectors:

        * ``e``: nonzero for any dates that produced errors, 0 otherwise.
            Shape = (len(self), len(jd)).
        * ``r``: position vectors in kilometers.
            Shape = (len(self), len(jd), 3).
        * ``v``: velocity vectors in kilometers per second.
            Shape = (len(self), len(jd), 3).

        Parameters
        ----------
        jd (float): Julian date.
        fr (float): Fractional part of the Julian date.

        Returns
        -------
        error (NDArray[np.uint8]): Error code.
        r (NDArray[np.float64]): Satellite position vector in km.
        v (NDArray[np.floating]): Satellite velocity vector in km/s.
        """
        ...
