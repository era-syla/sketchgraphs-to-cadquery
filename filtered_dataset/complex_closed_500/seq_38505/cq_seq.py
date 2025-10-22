import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02452, 0.062).lineTo(0.02452, 0.008).lineTo(0.03152, 0.062).lineTo(0.02452, 0.062).close()
solid=wp_sketch0.add(loop0).extrude(-0.015921877796544078)
