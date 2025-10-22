import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.4572, -0.3048).lineTo(0.4572, -0.3048).lineTo(0.4572, -0.6096).lineTo(-0.4572, -0.6096).lineTo(-0.4572, -0.3048).close()
solid=wp_sketch0.add(loop0).extrude(-2.287939598525603)
