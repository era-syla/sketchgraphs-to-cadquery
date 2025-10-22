import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03175, 0.03038).lineTo(0.04575, 0.03038).lineTo(0.04575, 0.02388).lineTo(0.03175, 0.02388).lineTo(0.03175, 0.03038).close()
solid=wp_sketch0.add(loop0).extrude(-0.010436971191808165)
