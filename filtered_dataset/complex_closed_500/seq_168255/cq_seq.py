import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00847, -0.02075).lineTo(-0.01, -0.02075).lineTo(-0.01, -0.01975).lineTo(-0.00847, -0.01975).lineTo(-0.00847, -0.02075).close()
solid=wp_sketch0.add(loop0).extrude(0.0003014006640451617)
