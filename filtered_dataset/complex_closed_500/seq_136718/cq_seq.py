import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02781, 0.107).lineTo(0.02719, 0.107).lineTo(0.02719, 0.092).lineTo(-0.01281, 0.092).lineTo(-0.01281, 0.052).lineTo(-0.02781, 0.052).lineTo(-0.02781, 0.107).close()
solid=wp_sketch0.add(loop0).extrude(-0.04360182614038919)
