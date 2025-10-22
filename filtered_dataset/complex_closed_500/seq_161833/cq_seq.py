import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03811, 0.01386).lineTo(0.06227, 0.01386).lineTo(0.06227, -0.01161).lineTo(0.03811, -0.01161).lineTo(0.03811, 0.01386).close()
solid=wp_sketch0.add(loop0).extrude(-0.06469975647693883)
