import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01568, -0.02705).lineTo(-0.01568, -0.02705).lineTo(-0.01568, 0.02705).lineTo(0.01568, 0.02705).lineTo(0.01568, -0.02705).close()
solid=wp_sketch0.add(loop0).extrude(0.12650790954804372)
