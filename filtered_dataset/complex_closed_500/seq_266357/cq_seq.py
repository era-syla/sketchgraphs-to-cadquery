import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.004, 0.07378).lineTo(0.004, 0.07378).lineTo(0.004, 0.07228).lineTo(0.0025, 0.07228).lineTo(0.0025, 0.06971).lineTo(-0.0025, 0.06971).lineTo(-0.0025, 0.07228).lineTo(-0.004, 0.07228).lineTo(-0.004, 0.07378).close()
solid=wp_sketch0.add(loop0).extrude(-0.0008454430990224963)
