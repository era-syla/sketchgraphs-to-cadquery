import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.08016, -0.02313).lineTo(-0.08206, -0.02313).lineTo(-0.08206, -0.02473).lineTo(-0.08016, -0.02473).lineTo(-0.08016, -0.02313).close()
solid=wp_sketch0.add(loop0).extrude(0.0008513395780449829)
