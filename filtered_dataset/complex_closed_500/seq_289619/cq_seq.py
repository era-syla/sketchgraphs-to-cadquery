import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.004, -0.23).lineTo(-0.004, -0.23).lineTo(-0.004, -0.22).lineTo(0.004, -0.22).lineTo(0.004, -0.23).close()
solid=wp_sketch0.add(loop0).extrude(-0.008905331069808614)
