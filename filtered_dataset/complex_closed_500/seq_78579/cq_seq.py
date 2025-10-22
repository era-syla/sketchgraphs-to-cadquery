import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.041, 0.00629).lineTo(0.019, 0.00629).lineTo(0.019, -0.07775).lineTo(-0.041, -0.07775).lineTo(-0.041, 0.00629).close()
solid=wp_sketch0.add(loop0).extrude(-0.13826537835356628)
