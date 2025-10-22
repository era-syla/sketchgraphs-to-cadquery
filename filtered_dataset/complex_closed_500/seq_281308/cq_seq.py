import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.028, 0.015).lineTo(-0.008, 0.015).lineTo(-0.008, 0.07).lineTo(-0.028, 0.07).lineTo(-0.028, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.09248303195392332)
