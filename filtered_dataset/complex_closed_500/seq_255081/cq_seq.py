import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.013, 0.0495).lineTo(0.013, 0.0495).lineTo(0.013, 0.0275).lineTo(-0.013, 0.0275).lineTo(-0.013, 0.0495).close()
solid=wp_sketch0.add(loop0).extrude(0.02931477382646511)
