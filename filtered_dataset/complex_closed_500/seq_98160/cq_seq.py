import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01967, 0.01977).lineTo(0.02015, 0.01977).lineTo(0.02015, -0.01913).lineTo(-0.01967, -0.01913).lineTo(-0.01967, 0.01977).close()
solid=wp_sketch0.add(loop0).extrude(0.012670642868450979)
