import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06823, 0.05136).lineTo(-0.00968, 0.05136).lineTo(-0.00968, 0.0037).lineTo(-0.06823, 0.0037).lineTo(-0.06823, 0.05136).close()
solid=wp_sketch0.add(loop0).extrude(0.10924686153036892)
