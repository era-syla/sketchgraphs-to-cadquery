import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02857, 0.03492).lineTo(0.02858, 0.03492).lineTo(0.02857, -0.03492).lineTo(-0.02857, -0.03492).lineTo(-0.02857, 0.03492).close()
solid=wp_sketch0.add(loop0).extrude(0.14965443938874623)
