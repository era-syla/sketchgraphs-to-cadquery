import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0097, 0.0132).lineTo(0.0097, 0.0033).lineTo(-0.0097, 0.0033).lineTo(-0.0097, 0.0132).lineTo(0.0097, 0.0132).close()
solid=wp_sketch0.add(loop0).extrude(-0.018550575661044528)
