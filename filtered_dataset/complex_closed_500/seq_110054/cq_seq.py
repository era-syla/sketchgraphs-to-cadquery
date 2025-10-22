import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0525, 0.05).lineTo(-0.0525, 0.037).lineTo(-0.0375, 0.037).lineTo(-0.0375, 0.05).lineTo(-0.0525, 0.05).close()
solid=wp_sketch0.add(loop0).extrude(0.021736368749267564)
