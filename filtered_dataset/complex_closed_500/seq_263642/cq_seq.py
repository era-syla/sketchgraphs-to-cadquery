import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.004, -0.002).lineTo(0.0032, -0.002).lineTo(0.0032, -0.003).lineTo(0.004, -0.003).lineTo(0.004, -0.002).close()
solid=wp_sketch0.add(loop0).extrude(-0.00010329607681920017)
