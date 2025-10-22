import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.085, -0.085).lineTo(-0.085, -0.085).lineTo(-0.085, 0.085).lineTo(0.085, 0.085).lineTo(0.085, -0.085).close()
solid=wp_sketch0.add(loop0).extrude(-0.38839212647095783)
