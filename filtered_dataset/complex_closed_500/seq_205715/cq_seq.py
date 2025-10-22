import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.9779, 0.01905).lineTo(-0.97155, 0.01905).lineTo(-0.97155, 0.00635).lineTo(-0.9779, 0.00635).lineTo(-0.9779, 0.01905).close()
solid=wp_sketch0.add(loop0).extrude(0.005959353305731949)
