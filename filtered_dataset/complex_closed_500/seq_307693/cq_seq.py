import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00143, 0.037).lineTo(0.02523, 0.037).lineTo(0.02523, 0.035).lineTo(0.00143, 0.035).lineTo(0.00143, 0.037).close()
solid=wp_sketch0.add(loop0).extrude(-0.020557349422260562)
