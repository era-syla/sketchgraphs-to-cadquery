import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.33).lineTo(0.025, 0.33).lineTo(0.025, 0.335).lineTo(0.0, 0.335).lineTo(0.0, 0.33).close()
solid=wp_sketch0.add(loop0).extrude(0.03372550579223015)
