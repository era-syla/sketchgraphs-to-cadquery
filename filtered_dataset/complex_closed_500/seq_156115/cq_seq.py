import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.038, -0.0165).lineTo(0.038, -0.0165).lineTo(0.038, 0.0165).lineTo(-0.038, 0.0165).lineTo(-0.038, -0.0165).close()
solid=wp_sketch0.add(loop0).extrude(0.19461418999325497)
