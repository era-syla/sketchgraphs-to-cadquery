import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04078, 0.03557).lineTo(0.01231, 0.01081).lineTo(0.01231, -0.001).lineTo(-0.04078, -0.001).lineTo(-0.04078, 0.03557).close()
solid=wp_sketch0.add(loop0).extrude(0.06541964569073008)
