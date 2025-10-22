import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04191, 0.03226).lineTo(0.02159, 0.03226).lineTo(0.02159, 0.02489).lineTo(0.04191, 0.02489).lineTo(0.04191, 0.03226).close()
solid=wp_sketch0.add(loop0).extrude(0.05393811565305772)
