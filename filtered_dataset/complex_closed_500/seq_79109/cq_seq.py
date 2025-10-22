import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03378, -0.00711).lineTo(0.03912, -0.00711).lineTo(0.03912, -0.02159).lineTo(0.03053, -0.02159).lineTo(0.03053, -0.00711).lineTo(0.03226, -0.00711).lineTo(0.03226, -0.01854).lineTo(0.03378, -0.01854).lineTo(0.03378, -0.00711).close()
solid=wp_sketch0.add(loop0).extrude(0.023035767421226077)
