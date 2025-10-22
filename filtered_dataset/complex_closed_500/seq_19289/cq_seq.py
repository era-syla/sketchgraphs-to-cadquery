import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0114, 0.024).lineTo(-0.03165, 0.024).lineTo(-0.03165, 0.026).lineTo(-0.0114, 0.026).lineTo(-0.0114, 0.024).close()
solid=wp_sketch0.add(loop0).extrude(0.025563604578836965)
