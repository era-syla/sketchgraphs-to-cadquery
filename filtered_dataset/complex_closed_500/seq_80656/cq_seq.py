import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02858, -0.04445).lineTo(-0.02857, -0.04445).lineTo(-0.02858, 0.04445).lineTo(0.02857, 0.04445).lineTo(0.02858, -0.04445).close()
solid=wp_sketch0.add(loop0).extrude(0.07397482375279447)
