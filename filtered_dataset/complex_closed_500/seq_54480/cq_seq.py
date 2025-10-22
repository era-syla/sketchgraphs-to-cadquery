import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00387, 0.0141).lineTo(0.00387, 0.0141).lineTo(0.00387, 0.01016).lineTo(-0.00387, 0.01016).lineTo(-0.00387, 0.0141).close()
solid=wp_sketch0.add(loop0).extrude(0.015573135954044637)
