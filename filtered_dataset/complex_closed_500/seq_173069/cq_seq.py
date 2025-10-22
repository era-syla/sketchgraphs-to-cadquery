import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01563, 0.0).lineTo(-0.00563, 0.0).lineTo(-0.00563, 1.0).lineTo(-0.01563, 1.0).lineTo(-0.01563, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(2.3459787316971683)
