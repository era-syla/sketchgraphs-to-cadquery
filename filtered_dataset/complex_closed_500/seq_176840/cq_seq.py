import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02825, -0.0146).lineTo(-0.02825, -0.01773).lineTo(-0.02212, -0.01773).lineTo(-0.02212, -0.01435).lineTo(-0.02024, -0.01435).lineTo(-0.02024, -0.02287).lineTo(-0.02212, -0.02287).lineTo(-0.02212, -0.01974).lineTo(-0.02825, -0.01974).lineTo(-0.02825, -0.02287).lineTo(-0.03026, -0.02287).lineTo(-0.03026, -0.01435).lineTo(-0.02825, -0.01435).lineTo(-0.02825, -0.0146).close()
solid=wp_sketch0.add(loop0).extrude(-0.028855209489874953)
