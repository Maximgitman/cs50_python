from um import count


def test_cases():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert (
        count(
            "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
        )
        == 2
    )


def test_um_included_word():
    assert count("Yummi") == 0
    assert count("Album") == 0
