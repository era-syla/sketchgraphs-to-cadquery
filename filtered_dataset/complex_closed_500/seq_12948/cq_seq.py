import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.34, 0.0).lineTo(-0.34, 0.025).lineTo(-0.14, 0.12).lineTo(0.0, 0.12).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.9665965991532216)
