from django.db import models
from model_utils.choices import Choices

from user_manager.models.address import Address
from user_manager.models.user_profile import Organization


class Exhibitor(models.Model):
    address = models.OneToOneField(Address)  # The address needs to be a global, shipping address.
    approved = models.BooleanField(default=False)

    name = models.CharField(max_length=100)
    CHAIN_CHOICES = Choices(
        "Alliance Cinemas",
        "Cine Enterprise",
        "Cinema Guzzo",
        "CineStarz",
        "Criterion",
        "Golden",
        "Hollywood 3",
        "Imagine Cinemas",
        "Landmark Cinemas",
        "Magic Lantern Theatres",
        "May",
        "OTG Cinemas",
        "Rainbow Cinemas",
        "RGFM",
        "Alamo Drafthouse Cinema",
        "Allen Theatres",
        "AMC",
        "Amstar/The Grand Theatre",
        "Apple Cinemas",
        "B&B Cinemas",
        "BarnZ's",
        "Barry Cinemas Inc",
        "Bow Tie Theatres",
        "Braden Theatre",
        "Brendan Theatres",
        "Caribbean Cinemas",
        "Carmike Cinemas",
        "Carolina Cinemas",
        "CEC Theatres",
        "Celebration Cinemas",
        "Center Cinemas",
        "Chunky's Cinema & Pub",
        "Cinebarre",
        "CineGrand",
        "Cinema Cafe",
        "Cinema City Theatres",
        "Cinema Latino",
        "Cinema West",
        "Cinema World",
        "CineMagic Theatres",
        "Cinemark",
        "Cinetopia",
        "Classic Cinemas",
        "Cobb Theatres",
        "Coming Attraction Theatres",
        "Consolidated Theatres",
        "Empire Cinemas",
        "Entertainment Cinemas",
        "Far Away Entertainment",
        "Flagship Cinemas",
        "Frank Theatres",
        "Franklin Theatre",
        "Fridley Theatres",
        "Galaxy Theaters",
        "Genju Theatres",
        "GHTC Theatres",
        "Goodrich Quality Theatres",
        "GTC Theatres",
        "Harkins Theatres",
        "High Sierra Theatres",
        "iPic Theatres",
        "Laemmie Theatres",
        "Latitude 30",
        "Logan Theatres",
        "Main Street Theatres",
        "Malco Theatres",
        "Marcus Theatres",
        "Marquee Cinemas",
        "Maya Cinemas",
        "Megaplex Theatres",
        "Metropolitan",
        "Mitchell Theatres",
        "Movie Tavern",
        "NGC Cinemas",
        "Nickelodeon Theatres",
        "Odyssey Theatres",
        "Omnimax",
        "P&G Theatres",
        "Paragon Theatres",
        "Patriot Cinemas",
        "Phoenix",
        "Picture Show",
        "Polson Theatres",
        "Premiere",
        "R/C Theatres",
        "Reading Cinemas",
        "Reel",
        "Regal",
        "Regency Cinemas",
        "Republic Theatres",
        "Rialto Cinemas",
        "Rogers Cinemas",
        "ShowBiz Cinemas",
        "Showcase Cinemas",
        "Showplace Cinemas",
        "Silver Screen Cinemas",
        "Smitty's Cinemas",
        "South Shore Cinemas",
        "Southeast Cinemas",
        "Starplex Cinemas",
        "Stone Theatres",
        "Studio Movie Grill",
        "Sun Basin Theatres",
        "Tristone Cinemas",
        "UEC Theatres",
        "UltraStar Cinemas",
        "Village Centre Cinemas",
        "Walker Theatres",
        "Warren Theatres",
        "Water Gardens",
        "Wehrenberg Theatres",
        "Westates Theatres",
        "Yakima Theatres",
        "Your Neighborhood Theatre",
    )
    chain = models.CharField(choices=CHAIN_CHOICES, max_length=100, blank=True)

    organization = models.ForeignKey(Organization, blank=True, null=True)

    def __unicode__(self):
        return self.name


class ScreeningRoom(models.Model):
    exhibitor = models.ForeignKey(Exhibitor)

    encryption = models.TextField()
    room_number = models.CharField(max_length=100)

    three_dimension_support = models.BooleanField(default=False, verbose_name='3D')
    closed_caption_support = models.BooleanField(default=False, verbose_name='CC')
    described_service_support = models.BooleanField(default=False, verbose_name='DS')
    imax_support = models.BooleanField(default=False, verbose_name='IMAX')
    atmos_support = models.BooleanField(default=False, verbose_name='ATMOS')
    dolby_seven_support = models.BooleanField(default=False, verbose_name='7.1')
    capacity = models.IntegerField(blank=True, null=True, verbose_name='Seating Capacity')
    screen_size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    four_k_support = models.BooleanField(default=False, verbose_name='4K')
    hfr_support = models.BooleanField(default=False, verbose_name='HFR')
    dbox_support = models.BooleanField(default=False, verbose_name='DBOX')

    media_block_serial_number = models.CharField(max_length=50)
    media_block_model = models.CharField(max_length=255)
    projector_model = models.CharField(max_length=255)
    projector_serial_number = models.CharField(max_length=50)