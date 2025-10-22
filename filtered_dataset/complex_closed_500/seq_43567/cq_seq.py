import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.6477, 2.032).lineTo(0.4953, 2.032).lineTo(0.4953, 0.0).lineTo(-0.6477, 0.0).lineTo(-0.6477, 2.032).close()
solid=wp_sketch0.add(loop0).extrude(-4.4121169578184105)
