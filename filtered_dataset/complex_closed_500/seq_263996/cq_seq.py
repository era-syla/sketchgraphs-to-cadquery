import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00135, 0.0).lineTo(0.0009, 0.00016).lineTo(0.0009, 0.0032).lineTo(0.001, 0.0033).lineTo(0.00165, 0.0033).lineTo(0.00175, 0.0032).lineTo(0.00175, 0.0028).lineTo(0.00147, 0.0028).lineTo(0.00147, 0.00014).lineTo(0.00136, -0.0).lineTo(0.00135, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.007540970639966713)
