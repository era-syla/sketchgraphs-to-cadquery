import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00414, 0.0265).lineTo(-6e-05, 0.0265).lineTo(-6e-05, 0.0165).lineTo(0.00414, 0.0165).lineTo(0.00414, 0.0265).close()
solid=wp_sketch0.add(loop0).extrude(-0.02929303534085107)
