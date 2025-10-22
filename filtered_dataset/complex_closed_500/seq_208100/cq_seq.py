import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-6.30535, 2.84).lineTo(-5.25645, 1.02325).lineTo(-5.22758, 1.07325).lineTo(-6.24761, 2.84).lineTo(-6.30535, 2.84).close()
solid=wp_sketch0.add(loop0).extrude(-5.216442507993373)
