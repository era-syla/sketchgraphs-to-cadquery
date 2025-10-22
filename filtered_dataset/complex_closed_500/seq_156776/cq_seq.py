import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0508, 0.09772).lineTo(0.02534, 0.09772).lineTo(0.02534, -0.02177).lineTo(-0.0508, -0.02177).lineTo(-0.0508, 0.09772).close()
solid=wp_sketch0.add(loop0).extrude(0.0030261889895995824)
