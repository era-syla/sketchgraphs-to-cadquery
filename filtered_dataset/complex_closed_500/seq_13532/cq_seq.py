import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02217, 0.04459).lineTo(0.02217, 0.03911).lineTo(-0.02217, 0.03911).lineTo(-0.02217, 0.04459).lineTo(0.02217, 0.04459).close()
solid=wp_sketch0.add(loop0).extrude(-0.0914687602833082)
