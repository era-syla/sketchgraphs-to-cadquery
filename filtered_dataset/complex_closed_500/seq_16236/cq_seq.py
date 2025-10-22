import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02687, 0.00602).lineTo(-0.01207, 0.00602).lineTo(-0.01207, -0.00698).lineTo(-0.02687, -0.00698).lineTo(-0.02687, 0.00602).close()
solid=wp_sketch0.add(loop0).extrude(0.0012117143330967126)
