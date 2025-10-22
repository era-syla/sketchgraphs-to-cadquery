import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0064, 0.0355).lineTo(-0.005, 0.0355).lineTo(-0.005, 0.0245).lineTo(-0.0064, 0.0245).lineTo(-0.0064, 0.0355).close()
solid=wp_sketch0.add(loop0).extrude(0.032028868695491326)
