import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03174, -0.02338).lineTo(-0.03378, -0.02338).lineTo(-0.03378, -0.01832).lineTo(-0.03174, -0.01832).lineTo(-0.03174, -0.02338).close()
solid=wp_sketch0.add(loop0).extrude(0.01202978011211192)
