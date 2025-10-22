import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05378, 0.04194).lineTo(0.05438, 0.04194).lineTo(0.05438, -0.04984).lineTo(-0.05378, -0.04984).lineTo(-0.05378, 0.04194).close()
solid=wp_sketch0.add(loop0).extrude(0.13270912758745776)
