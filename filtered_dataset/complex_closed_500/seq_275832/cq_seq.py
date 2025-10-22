import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03937, 0.0).lineTo(-0.01969, 0.0).lineTo(-0.01969, -0.01969).lineTo(-0.03937, -0.01969).lineTo(-0.03937, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.04543907211835462)
