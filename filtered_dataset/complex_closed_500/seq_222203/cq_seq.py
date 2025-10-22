import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0305, -0.0085).lineTo(0.028, -0.0085).lineTo(0.028, -0.0065).lineTo(0.0305, -0.0065).lineTo(0.0305, -0.0085).close()
solid=wp_sketch0.add(loop0).extrude(-0.0017254470943961246)
